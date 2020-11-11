var player, ball, ai;

var playerScore = 0;
var AIScore = 0;

var dots = [];
var dSize = 10;
var txtSize = 30;

function setup(){
    createCanvas(800,500)

    player = new Player;
    ai = new AI();
    ball = new Ball();
    for(let y = dSize/2; y<height; y+=dSize*2){
        dots.push(createVector(width/2-dSize/2, y));

    }
}

function draw(){
    background(0);

    noStroke();
    fill(255, 100)
    drawSquares();

    ball.update();
    ball.show();

    player.update();
    player.show();

    ai.update();
    ai.show(); 



    drawScores();
}

function drawScores(){
    let x1 = width/4;
    let x2 = width*3/4;
    let y = txtSize*1.5;

    noStroke()
    fill(255);
    textAlign(CENTER);
    textSize(txtSize)
    textSize((playerScore), x1, y);
    textSize((AIScore), x2, y)
}

function drawSquares(){
    for(let i = 0; i<dots.length; i++){
        let x = dots[i].x;
        let y = dots[i].y;

        rect(x,y,dSize,dSize)
    }
}

function keyPress(){
    if(key == 'W' || keyCode== UP_ARROW){
        player.up();
    }else if(key == 'S' || keyCode== DOWN_ARROW){
        player.down();
}

function KeyReleased(){
    if((key == 'W' || keyCode== UP_ARROW)|| (key == 'S' || keyCode== DOWN_ARROW)){
        player.stp();
    }}
} 


function Player(){
    this.w = 15;
    this.h = 80;

    this.pos =createVector(this.w*2, height/2-this.h/2);
    this.acc =createVector(0,0);
    this.spd = 10;
    this.maxSpd = 10;

    this.show = function(){
        noStroke();
        fill(255);
        rect(this.pos.x, this.pos.y, this.w, this.h);
    }

    this.up = function(){this.acc.y-=this.spd;}
    this.down = function(){this.acc.y+=this.spd;}
    this.stop = function(){this.acc.y = 0;}

    this.update = function(){
        this.acc.y= constrain(this.acc.y, -this.maxSpd, this.maxSpd);
        this.pos.add(this.acc);
        this.pos.y = constrain(this.pos.y, 0 , height-this.h);
    }
}

function Ball(){
    this.pos = createVector(width/2,height/2);
    this.r = 10;
    this.maxSpd = createVector(20,15);
    
    do{
      this.acc = p5.Vector.random2D();
      this.acc.setMag(random(4,6));
    }while(abs(this.acc.x)<3 || abs(this.acc.y)<3);

    this.show = function(){
        noStroke();
        fill(255);
        ellipse(this.pos.x, this.pos.y, this.r*2);

    }

    this.update = function(){
        this.pos.add(this.acc);

        if(this.pos.y<this.r || this.pos.y>height-this.r){
            this.acc.y*=-1;
        }
    }

}


function AI(){
    this.w = player.w;
    this.h = player.h;
    this.pos = createVector(width-this.w*3, height/2-this.h/2);
    this.acc = createVector(0,0);
    this.spd = 10;

    this.show = function(){
        noStroke();
        fill(255);
        rect(this.pos.x, this.pos.y, this.w, this.h);
    
    }
    this.update = function(){
        let d1 =dist(ball.pos.x, ball.pos.y, this.pos.x, this.pos.y);
        let d2 =dist(ball.pos.x, ball.pos.y, this.pos.x, this.pos.y+this.h);
        let d = (d1+d2)/2;

        this.pos.add(this.acc);
        this.pos.y = constrian(this.pos.y, 0, height-this.h);

        if(d<450){
            if(ball.pos.y<this.pos.y-this.h/2){
                this.acc.y-=this.spd;
            }else{
                this.acc.y+=this.spd;
            
            }

            this.acc.y= constrain(this.acc.y, -this.maxSpd, this.maxSpd);
        }else{
            this.acc.y+=random(-this.spd*0.9, this.spd)
        
        }

    }
}

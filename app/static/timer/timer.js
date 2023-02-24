

//defines how big the circle arc of the timer should be
function setTimerProgress(progress) {
    progress=1-progress;
    $("#timer").removeClass("border-bg").removeClass("border-sm");
    if (progress<0.5) {
        $("#timer").addClass("border-sm");
    } else {
        $("#timer").addClass("border-bg");
    }

    $("#timer").attr("style","--progress:"+progress+";");
}

//text inside timer
/**
 * 
 * @param {string} display 
 * text inside the timer !
 */
function setTimerDisplay(display) {
    $("#timer-value").html(display);
}

setTimerProgress(0);

/**
 * redefine the function, it will be called when the timer comes to an end !
 */
function onComplete() {
    console.log("done !");
}


var timer_paused = false;
/**
 * 
 * @param {int} seconds
 * starts the countdown from the time displayed. Calls onComplete when countdown reaches 0. 
 */
function startTimer(seconds) {
    var time = seconds;
    const deltatime=0.1;
    var over = false;
    
    function updateTimer() {
        if (timer_paused) {
            return;
        }
        if (!over) {
            time = time-deltatime;
            if (time<0) {
                time=0;
                over=true;
                onComplete();
            }
            setTimerProgress(1-time/seconds);
            setTimerDisplay(Math.ceil(time));
        }
        
    }

    setInterval(updateTimer,1000*deltatime);
}

function pauseTimer() {
    timer_paused=true;
}

function resumeTimer() {
    timer_paused=false;
}

/**
 * pause the timer if it is running, resume if it isn't
 */
function pause_unpause() {
    if (timer_paused) {
        resumeTimer();
    } else {
        pauseTimer();
    }
}

function triggerAlarm(repetitions) {
    console.log("Alarm may be muted by Chrome if the user hasn't interacted with the website yet...");
    var audio = new Audio('../static/timer/ping.mp3');
    for (i=0; i<repetitions; i++) {
        audio.play();
    }
    
}
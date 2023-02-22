

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

function triggerAlarm(repetitions) {
    console.log("Alarm may be muted by Chrome if the user hasn't interacted with the website yet...");
    var audio = new Audio('../static/timer/ping.mp3');
    for (i=0; i<repetitions; i++) {
        audio.play();
    }
    
}
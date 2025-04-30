
let recognition;

function startDictation() {
    if ('webkitSpeechRecognition' in window) {
        recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';
        recognition.lang = 'hi-IN';

        document.getElementById('mic-status').style.display = 'block'; // show mic

        recognition.start();

        recognition.onresult = function(event) {
            document.getElementById('text').value = event.results[0][0].transcript;
            recognition.stop();
            document.getElementById('mic-status').style.display = 'none';
        };

        recognition.onerror = function(event) {
            alert('Error: ' + event.error);
            recognition.stop();
            document.getElementById('mic-status').style.display = 'none';
        };

        recognition.onend = function() {
            document.getElementById('mic-status').style.display = 'none';
        };

    } else {
        alert("Your browser doesn't support speech recognition. Try using Chrome.");
    }
}


/* Script functions for game assets page */

/* Function to only allow one audio asset to be played at a time */
function onlyPlayOneIn(container) {
    container.addEventListener("play", function(event) {
    audio_elements = container.getElementsByTagName("audio")
        for (i=0; i < audio_elements.length; i++) {
            audio_element = audio_elements[i];
            if (audio_element !== EventTarget) {
                audio_element.pause();
            }
        }
    }, true);
}

/* Run function, pass entire document body as container */
document.addEventListener("DOMContentLoaded", function() {
    onlyPlayOneIn(document.body);
});

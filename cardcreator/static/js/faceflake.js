var FLAKE_SIZE = 45; // Constant to change the size of the flake
var MAX_FLAKE_SPEED = 5; // Constant to change the max speed the flakes fall
var MIN_FLAKE_SPEED = 3; // Constant to change the min speed the flakes fall
var flake_speeds = [];

// Detect faces after photos have loaded
$(document).ready(function() {
  var tmpImg = new Image();
  tmpImg.src = $("#photo").attr("src");
  tmpImg.onload = function() {
    $("#photo").faceDetection({
      complete: function(faces) {
        createFlakes(faces);
      }
    })
  }
});

function createFlakes(faces) {
  // We don't want to process the following code if there were no faces detected
  if (faces.length == 0)
    return; 

  // Loop through each face found and create a corresponding snow-flake
  // We adjust the width, height, left, top CSS attributes of the flake img to match up to the snow flake's width/height
  for(var i=0;i<faces.length;i++) {
    face = faces[i];

    var flake = $("<div class='snow-flake'><img src='" + $("#photo").attr("src") +"' /></div>");
    flake.css("left", Math.random() * ($(document).width() - FLAKE_SIZE));

    var originalWidth = $("#photo").width() / face.scaleX,
        newWidth = originalWidth * FLAKE_SIZE / face.width;
        originalHeight = $("#photo").height() / face.scaleY,
        newHeight = originalHeight * FLAKE_SIZE / face.height,
        newX = face.x * (newWidth/originalWidth),
        newY = face.y * (newHeight/originalHeight);

    flake.children("img").css({
      'width': newWidth + 'px',
      'height': newHeight + 'px',
      'left': (newX * -1) + 'px',
      'top': (newY * -1) + 'px'
    });
    $('body').append(flake);

    flake_speeds.push(Math.random() * (MAX_FLAKE_SPEED - MIN_FLAKE_SPEED) + MIN_FLAKE_SPEED);
  }

  // Every 30ms, move the flakes
  setInterval("moveFlakes()", 30);
}

// When called, each snow flake in the DOM is moved down
// If they reach the bottom of the page, they are moved back up and have their X axis shifted
function moveFlakes() {
  $(".snow-flake").each(function(i) {
    $(this).css("top", $(this).position().top + flake_speeds[i]);

    if ($(this).position().top >= $(window).height() + FLAKE_SIZE) {
      $(this).css("top", -FLAKE_SIZE);

      $(this).css("left",  Math.random() * ($(document).width() - FLAKE_SIZE));
    }
  })
}

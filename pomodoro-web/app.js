const FOCUS = 25 * 60;
const BREAK = 5 * 60;

const clock = document.getElementById("clock");
const phaseLabel = document.getElementById("phase");
const toggle = document.getElementById("toggle");
const reset = document.getElementById("reset");

let remaining = FOCUS;
let breaking = false;
let ticker = null;

function render() {
  const m = String(Math.floor(remaining / 60)).padStart(2, "0");
  const s = String(remaining % 60).padStart(2, "0");
  clock.textContent = `${m}:${s}`;
  phaseLabel.textContent = breaking ? "Break" : "Focus";
}

function tick() {
  remaining -= 1;
  if (remaining < 0) {
    breaking = !breaking;
    remaining = breaking ? BREAK : FOCUS;
  }
  render();
}

toggle.addEventListener("click", () => {
  if (ticker) {
    clearInterval(ticker);
    ticker = null;
    toggle.textContent = "Start";
  } else {
    ticker = setInterval(tick, 1000);
    toggle.textContent = "Pause";
  }
});

reset.addEventListener("click", () => {
  clearInterval(ticker);
  ticker = null;
  toggle.textContent = "Start";
  breaking = false;
  remaining = FOCUS;
  render();
});

render();

const fortunes = [
    {
        fortune: "You will have a great day!",
        color: "blue"
    },
    {
        fortune: "You will be able to remember how to link CSS in HTML next time!",
        color: "green"
    },
    {
        fortune: "Your hard work will soon pay off.",
        color: "gold"
    },
    {
        fortune: "You will NOT remember how to center a div.",
        color: "red"
    },
    {
        fortune: "You will find what you are looking for.",
        color: "purple"
    },
    {
        fortune: "You will find that bug soon!",
        color: "orange"
    }
];

function randomFortune(){
    choice = fortunes[Math.floor(Math.random() * 7)]
    document.getElementById("magicBall").innerHTML = choice.fortune
    document.getElementById("magicBall").style.color = choice.color    
}

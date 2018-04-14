function headerMode(bool) {
    if (bool){
        document.getElementById("titleDisplay").innerText = 'A Watched Pot Never Boils'
    }
    else {
        document.getElementById("titleDisplay").innerText = 'An Unwatched Pot Never Boils'
    }
}


function refresh(node) //may or may not work
{
    const times = 5000; // gap in Milli Seconds;

    (function startRefresh()
    {
        address = node.src;
        node.src = address;
        setTimeout(startRefresh,times);
    })();

}

window.onload = function()
{
    const node = document.getElementById("photoFound");
    refresh(node);
    // you can refresh as many images you want just repeat above steps
};
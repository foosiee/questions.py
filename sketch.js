function setup(){
	
	noCanvas();
	
	var x;
	var p;
	
	var tCounter = 0;
	var nCounter = 0;
	var aCounter = 0;
	
	var noAnswers = select("#noanswer");
	var answers = select("#answer");
	var total = select("#total");
	var percentage = select("#percentage");
	
	var bar = document.getElementById("myBar");
	var width = 0;
	
	document.onkeypress = function(){keyPress(x)};
	document.getElementById("button").onmousedown = function(){reset()};
	
	function reset(){
		tCounter = 0;
		nCounter = 0;
		aCounter = 0;
		updateHTML();
		calculatePercent();
	}
	
	function subAns(){
		if(tCounter > 0 && nCounter > 0 && aCounter > 0){
			nCounter++;
			aCounter--;
			updateHTML();
		}
	}
	
	function subNo(){
		if(tCounter > 0 && nCounter > 0 && aCounter > 0){
			nCounter--;
			aCounter++;
			updateHTML();
		}
	}
	
	function update(k){
		k++;
		updateTotal(1);
		updateHTML();
		return k;
	}
	
	function updateTotal(){
		tCounter++;
	}
	
	function calculatePercent(){
		p = round((aCounter / tCounter) * 100);
		if(isNaN(p)){
			p = 0;
		}
		updateHTML();
	}
	
	function updateHTML(){
		total.html("total questions: " + tCounter);
		answers.html("answered questions: " + aCounter);
		noAnswers.html("unanswered questions: " + nCounter);
		bar.style.width = p + '%';
		bar.innerHTML = p + "%";
		if (p <= 79 && p >= 60){
			bar.style.backgroundColor = 'yellow';
		}
		else if (p < 60){
			bar.style.backgroundColor = 'red';
		}
		else{
			bar.style.backgroundColor = '#4CAF50';
		}
	}
	
	function keyPress(x){
		x = event.keyCode;
		console.log(x);
		
		if(x == 113){
			nCounter = update(nCounter);
		}
		else if(x == 97){
			aCounter = update(aCounter);
		}
		else if(x == 119){
			subNo();
		}
		else if(x == 115){
			subAns();
		}
		calculatePercent();
	}
}
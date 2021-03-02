// Question 1
    function calculate(min, max){
        let total = 0;
        while(min <= max){        
            total = total + min ;
            min++;
        }
        console.log(total);
    }    
    
    calculate(1, 3)
    // 你的程式要能夠計算 1+2+3，最後印出 6  
    calculate(4, 8)
    // 你的程式要能夠計算 4+5+6+7+8，最後印出 30


// Question 2 要求二：Python字典與列表、JavaScript物件與陣列完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。提醒：​請勿更動題目中任何已經寫好的程式。要求二：Python字典與列表、JavaScript物件與陣列完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。提醒：​請勿更動題目中任何已經寫好的程式。

function avg(data){
    
    let employees_number = data["employees"].length;
    let total = 0;

    //  應該也可能以 for in 來處理 
    for(let i=0 ; i < employees_number; i++){
        total = total + data["employees"][i]["salary"]
    }
    
    let average = total / employees_number;

    console.log(average)


    

}

avg(
    {"count":3,
        "employees":[
                    {"name":"John","salary":30000},
                    {"name":"Bob","salary":60000},
                    {"name":"Jenny","salary":50000}
                ]
        }
    )

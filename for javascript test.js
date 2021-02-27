// for javascript test

// function announceThatIAmDoingImportantWork(){
//     console.log("I’m doing very important work!");
// };

// announceThatIAmDoingImportantWork();


// const busy = announceThatIAmDoingImportantWork;
//  busy()
// // console.log(busy);


// let i = 2;
// let j =[];
// const if_test = () =>{
//     if(i === 2){
//         console.log("it is 2")
//         j.push(i);
//     }

//     if(i == 2){
//         console.log("it is not 1");
//         j.push(i);
//     }
//     console.log(j.toLocaleString())
// }

// if_test();


function Tree(name) {
    this.name = name
  }
  
  let theTree = new Tree('Redwood')
  console.log(theTree.name)
  console.log("Hello!")
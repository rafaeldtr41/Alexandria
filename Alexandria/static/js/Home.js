'use strict'





function All_Visible(aux){
    // Giving a array of html table <th> elements turns all visible
    for (let i=0; i < aux.length; i++){

        aux[i].style.visibility = 'visible';
    }

}


function All_Hiden(aux){
    // Giving a array of html table <th> elements turns all hidden
    for (let i=0; i< aux.length; i++){

        aux[i].style.visibility = 'hidden';
    }

}


function get_all(){
    // Returns all html table <th> elements
    let tableId = document.getElementById('elements').getElementsByTagName('tbody')[0].getElementsByTagName('tr');
    return tableId;

}


function get_selected(content){
    //Giving a string returns all html table <th>  who has content who coincide with this string
    let elements = get_all();
    let aux = NaN;
    let to_hide = [];
    let to_visible = [];
    let bool = false 
    
    for (let i=0; i< elements.length; i++){

        aux = elements[i].getElementsByTagName('th');

        for (let j = 0; j< aux.length; j++){

            
            if (aux[j].innerHTML.includes(content)){
                bool = true;
                break;
            }
        }

        if (bool){
            to_visible.push(elements[i]);
            bool = false;
        }else{
            to_hide.push(elements[i]);
        }
    }
    All_Hiden(to_hide);
    // Turns all visible just in case :)
    return All_Visible(to_visible);

}

function search(){

    
    let word = document.getElementById("search-bar").value
    
    if(word === ''){

        return All_Visible(get_all());
    }

    return get_selected(word);

}

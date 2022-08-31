// let petSpecieSelection = document.getElementById('pet_specie');
let petSpecieSelection = document.getElementsByName('pet_specie');
let primaryBreedSelection = document.getElementById('primary_breed');


for (selection of petSpecieSelection){
        
    selection.addEventListener("click", function(event){
            
        petSpecieID = event.target.value;

        fetch(`/api/breeds/${petSpecieID}`).then(function(response){

            response.json().then(function(data){
                    
                breedOptionHTML = '';

                for(let breed of data.breeds) {
                        
                    breedOptionHTML += `<option values="${breed.id}">${breed.breed_name}</option>`;

                }

                primaryBreedSelection.innerHTML = breedOptionHTML;

            });

        });
    });

}

# webfortune

Final project for Dev Ops class.


#Usage for git clone
git clone https://github.com/Conbrown100/webfortune

Run your flask environment [python3 -m flask run --host=0.0.0.0]

#Usage for Docker image

docker pull conbrown100/webfortune


#Once cloned or pulled

url routes 

/fortune/ - returns a random fortune for the user to view
/cowsay/[input cowsay] - user inputs what cowsay will say. Then is returned cowsay on their screen.
/cowfortune/ - cowsay is automatically input a random fortune just like in /fortune/ but now cowsay says it.

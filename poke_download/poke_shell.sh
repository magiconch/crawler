python pokemon.py >> poke_url
cat poke_url | while read myline
do
 you-get $myline
done
rm poke_url

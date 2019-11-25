docker run -it --rm -v `pwd`/docs:/doc -e USER_ID=$UID ddidier/sphinx-doc:2.2.1-1 make clean html

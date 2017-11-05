# cleaner-cli
A command line interface that keeps your otherwise messy desktop presentable. Installations should be as simple as forking or downloading and then

```
pip install "path/to/your/local/repo"
```  
After installing you can run
```
cd folder/to/clean
clean -f "filetypes"
```
to tidy up the folder you're currently in. Specifically running this will take any files with the extentions you've given in `-f` and place them in a subfolder named according to the filetype. So for example you could run

```
cd c:/.../desktop
clean -f "pdf,txt,docx,xls"
```

Also this is very much in development, and not very useful after all.

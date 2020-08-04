:: !!Modify it as your local hugo path!!
SET HugoPath="C:\Projects\aspose.nanjing.documents\hugo-0.73\hugo.exe"

rem "Deal with git content: %time%"
git checkout .
git pull

rem "Begin to run hugo command: %time%"
:: %HugoPath% --minify --config config.toml --destination ..\public_cells
rem "Hugo command run finished. %time%"

rem "Start to pack site..."
tar -zcvf public_cells.tar.gz public_cells/*
rem "pack site finished. %time%"
:: tar -xzvf public_cells.tar.gz -C tmp

rem "Transmit tar.gz to server VM..."
:: scp -i deploy_key.key public_cells.tar.gz laurencechen@44.230.76.109:/var/www/docs.aspose.com/html




:: rem "Start to clean old cells site.."
:: ssh -i deploy_key.key laurencechen@44.230.76.109 "rm -rf /var/www/docs.aspose.com/html/cells/*"

:: rem "Start to deploy new cells site.."
:: scp -i deploy_key.key -r public_cells/* laurencechen@44.230.76.109:/var/www/docs.aspose.com/html/cells

rem "Deploy finished. All task complete."

pause
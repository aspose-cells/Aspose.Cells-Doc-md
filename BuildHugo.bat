:: Modify it as your hugo path!
SET HugoPath="C:\Projects\aspose.nanjing.documents\hugo-0.73\hugo.exe"

rem "Begin to run hugo command.."
HugoPath --minify --config config.toml
rem "Hugo command run finished."

rem "Start to clean old cells site.."
ssh -i deploy_key.key laurencechen@44.230.76.109 "rm -rf /var/www/docs.aspose.com/html/cells/*"

rem "Start to deploy new cells site.."
scp -i deploy_key.key -r public/* laurencechen@44.230.76.109:/var/www/docs.aspose.com/html/cells
rem "Deploy finished. All task complete."

pause
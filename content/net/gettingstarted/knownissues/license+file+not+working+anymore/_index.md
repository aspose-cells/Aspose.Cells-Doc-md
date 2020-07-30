---
title : "License File Not Working Anymore" 
description : "" 
weight : 12028 
toc : false
type: docs
url: /net/gettingstarted/knownissues/license+file+not+working+anymore/
---

# Aspose.Cells for .NET : License File Not Working Anymore


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Symptom](#symptom)
    *   1.1 [A Scenario](#a-scenario)
    *   1.2 [Solution](#solution)
    *   1.3 [Confirmation](#confirmation)
    *   1.4 [References](#references)
{{< /panel >}}
## Symptom

Sometimes, the users get frustrated for their license files do not work any longer when they move / publish their web project(s) to a new server. They feel upset as their license files were working properly on their previous (old) server but now they get an extra **Evaluation Copyright Warning** watermark Worksheet (whenever they generate reports using the component) on the new server environment.

### A Scenario

"We have been using Aspose.Cells on our ASP.NET web project to generate/manipulate Excel reports, we got a valid license that we are using. Some days ago, we moved the website to a new server; there were no upgrades or changes whatsoever, we have made sure and simply moved each and every file to the new server, including the Aspose.Cells.dll and related .lic file(s). Now when we try to generate Excel reports in the new server environment, we get an **Evaluation Copyright Warning** watermark sheet on our reports. We did try downloading and installing a new license file from My Orders section of the site, but it did not fix the problem at all. FYI, we implement the license by placing the Aspose.Cells.lic file in the site's bin folder along with the Aspose.Cells.dll component file, which, as I have mentioned, worked with no problem on the old server."

### Solution

Aspose has a clean and reliable licensing mechanism. Generally, the issue should be related to deployment problem. If a license file works fine (on a server), it should work equally fine on other servers / environments too. Normally the users utilize Application\_Start or Session\_Start events etc. in the global.asax file to place the licensing code there. So, it is quite possible that the Application\_Start / Session\_Start event(s) isn't fired to process the licensing code on their new location(s). It is to be noted here, Aspose.Cells will always throw an exception if the component cannot find the license file in a path. The users should make sure that licensing code (wherever they place) should be processed and events should be triggered in which the put the licensing code. The user can re-start the related service i.e.., "World Wide Web Publishing" and try to trace whether Application\_Start  / Session\_Start events get triggered when they visit their projects on the new server environment.

### Confirmation

Please also make sure that…

*   You are using a valid license file in your project.
*   You or somebody else should not edit / modify the license file least the license file will not work.
*   You should be aware of your license subscription expiry (you may simply open the lic file into notepad and check the expiry date).
*   You are not using a version (Aspose.Cells.dll) which is released after your license subscription expiry. It is to be noted here, a license file never expires, but if you are using the component version that are released after your subscription expiry, you will get an extra **Evaluation Copyright Warning** watermark sheet whenever you create an excel file.

### References

[http://www.aspose.com/community/forums/thread/156770.aspx](http://www.aspose.com/community/forums/thread/156770.aspx)

[http://www.aspose.com/community/forums/thread/155268/license-not-being-detected.aspx](http://www.aspose.com/community/forums/thread/155268/license-not-being-detected.aspx)  


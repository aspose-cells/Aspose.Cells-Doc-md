---
title: License File Not Working Anymore
type: docs
weight: 60
url: /net/license-file-not-working-anymore/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Symptom**

Sometimes, users get frustrated because their license files do not work any longer when they move/publish their web project(s) to a new server. They feel upset because their license files were working properly on their previous (old) server, but now they get an extra **Evaluation Copyright Warning** watermark worksheet (whenever they generate reports using the component) in the new server environment.

### **A Scenario**

"We have been using Aspose.Cells in our ASP.NET web project to generate/manipulate Excel reports, and we have a valid license. A few days ago, we moved the website to a new server; there were no upgrades or changes whatsoever. We made sure to copy every file to the new server, including the Aspose.Cells.dll and related .lic file(s). Now, when we try to generate Excel reports in the new server environment, we get an **Evaluation Copyright Warning** watermark sheet on our reports. We tried downloading and installing a new license file from the My Orders section of the site, but it did not fix the problem at all. For your information, we implement the license by placing the Aspose.Cells.lic file in the site's bin folder along with the Aspose.Cells.dll component file, which, as mentioned, worked with no problem on the old server."

### **Solution**

Aspose has a clean and reliable licensing mechanism. Generally, the issue is related to deployment. If a license file works fine on one server, it should work equally well on other servers/environments. Normally, users place the licensing code in the `Application_Start` or `Session_Start` events in the `Global.asax` file. Therefore, it is possible that the `Application_Start`/`Session_Start` event(s) are not being fired on the new server, preventing the licensing code from executing. Note that Aspose.Cells will always throw an exception if the component cannot find the license file at the specified path. Users should ensure that the licensing code (wherever it is placed) is executed and that the relevant events are triggered. The user can restart the related service, i.e., **World Wide Web Publishing Service**, and verify whether `Application_Start` / `Session_Start` events are triggered when they access the project on the new server.

### **Confirmation**

Please also make sure that…

- You are using a valid license file in your project.
- You or anyone else should not edit/modify the license file, otherwise it will not work.
- You should be aware of your license subscription expiry (you can simply open the `.lic` file in Notepad and check the expiry date).
- You are not using a version of `Aspose.Cells.dll` that was released after your license subscription expired. Note that a license file never expires, but if you use a component version released after your subscription expiry, you will get an extra **Evaluation Copyright Warning** watermark sheet whenever you create an Excel file.

### **References**

<https://forum.aspose.com/t/license-file-not-working-on-new-server/83110>

<https://forum.aspose.com/t/license-not-being-detected/83516/4>
{{< app/cells/assistant language="csharp" >}}

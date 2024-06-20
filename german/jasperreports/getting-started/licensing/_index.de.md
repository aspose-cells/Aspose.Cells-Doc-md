---
title: Lizenzierung
type: docs
weight: 40
url: /de/jasperreports/licensing/
---

{{% alert color="primary" %}}

Aspose.Cells for JasperReports ist als kostenlose, zeitlich unbegrenzte Evaluierung vom [Download-Portal](https://downloads.aspose.com/cells/jasperreports) verfügbar. Die Evaluierungsversionen und lizenzierten Versionen des Produkts sind der gleiche Download.

Wenn Sie mit der Evaluierungsversion zufrieden sind, können Sie eine [Lizenz erwerben](https://purchase.aspose.com/). Stellen Sie sicher, dass Sie die Lizenzvereinbarungen verstanden haben und diesen zustimmen.

Die Lizenz ist zum Download auf der Bestellseite verfügbar, sobald die Bestellung bezahlt wurde. Die Lizenz ist eine Klartext, digital signierte XML-Datei. Die Lizenz enthält Informationen wie den Client-Namen, das gekaufte Produkt und den Lizenztyp. Ändern Sie den Inhalt der Lizenzdatei nicht, da dies die Lizenz ungültig macht.

Es gibt zwei Möglichkeiten, eine Lizenz anzuwenden:

- [Rufen Sie setLicense auf](/cells/de/jasperreports/licensing/#call-setlicense)
- [Setzen Sie einen Exportparameter in applicationContext.xml](/cells/de/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

Nach der Installation der Lizenz,

- [Überprüfen Sie, ob es funktioniert](/cells/de/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **Rufen Sie setLicense auf**

{{% alert color="primary" %}}

Diese Methode ist für die Verwendung mit JasperReports geeignet.

{{% /alert %}}

Laden Sie die Lizenz auf Ihren Computer herunter und kopieren Sie sie in den entsprechenden Ordner (zum Beispiel den Anwendungsordner oder **JasperReports\lib**).
Fügen Sie den folgenden Code in Ihr Projekt ein:

{{< highlight csharp >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **Legen Sie das Lizenzdatei-Exportparameter in applicationContext.xml fest.**

{{% alert color="primary" %}}

Diese Methode ist für die Verwendung mit JasperServer geeignet.

{{% /alert %}}

1. Download the license to your computer and copy it to the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF** folder, where **\<InstallDir>** stands for the JasperServer installation directory.
1. Locate the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** file and add the following lines:

**XML**

{{< highlight csharp >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **Überprüfen Sie, ob die Lizenz funktioniert**

Exportieren Sie einen Bericht in das XLS-Format und prüfen Sie, ob der Bericht eine Evaluierungsnachricht enthält. Wenn keine Evaluierungsnachricht vorhanden ist, funktioniert die Lizenz ordnungsgemäß.

**Aspose.Cells for JasperReports fügt ein Bewertungsarbeitsblatt im Evaluierungsmodus ein** 

![todo:image_alt_text](licensing_1.png)

**Wenn eine gültige Lizenz vorhanden ist, gibt es kein Bewertungsarbeitsblatt** 

![todo:image_alt_text](licensing_2.png)

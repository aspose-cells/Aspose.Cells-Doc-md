---
title: Lizenzierung
type: docs
weight: 40
url: /de/jasperreports/licensing/
---
{{% alert color="primary" %}}

 Aspose.Cells for JasperReports ist als kostenlose, zeitlich unbegrenzte Auswertung bei der erhältlich[Download-Seite](https://downloads.aspose.com/cells/jasperreports). Die Testversion und die lizenzierte Version des Produkts sind derselbe Download.

 Wenn Sie mit der Evaluierungsversion zufrieden sind, können Sie dies tun[eine Lizenz erwerben](https://purchase.aspose.com/). Stellen Sie sicher, dass Sie die Lizenzbedingungen verstanden haben und ihnen zustimmen.

Die Lizenz steht nach Bezahlung der Bestellung auf der Bestellseite zum Download bereit. Die Lizenz ist eine digital signierte XML-Datei im Klartext. Die Lizenz enthält Informationen wie den Kundennamen, das erworbene Produkt und den Lizenztyp. Ändern Sie nicht den Inhalt der Lizenzdatei: Dadurch wird die Lizenz ungültig.

Es gibt zwei Möglichkeiten, eine Lizenz zu beantragen:

- [Rufen Sie setLicense auf](/cells/de/jasperreports/licensing/#call-setlicense)
- [Legen Sie einen Exporter-Parameter in applicationContext.xml fest](/cells/de/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

Nachdem Sie die Lizenz installiert haben,

- [Überprüfen Sie, ob es funktioniert](/cells/de/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **Rufen Sie setLicense auf**

{{% alert color="primary" %}}

Diese Methode ist für die Verwendung mit JasperReports anwendbar.

{{% /alert %}}

 Laden Sie die Lizenz auf Ihren Computer herunter und kopieren Sie sie in den entsprechenden Ordner (zum Beispiel den Ordner Ihrer Anwendung oder**JasperReports\lib**).
Fügen Sie Ihrem Projekt den folgenden Code hinzu:

{{< highlight "csharp" >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **Legen Sie den Parameter „licenseFile Exporter“ in „applicationContext.xml“ fest**

{{% alert color="primary" %}}

Diese Methode gilt für die Verwendung mit JasperServer.

{{% /alert %}}

1.  Laden Sie die Lizenz auf Ihren Computer herunter und kopieren Sie sie in die**\<Installationsverzeichnis>\apache-tomcat\webapps\jasperserver\WEB-INF**Ordner, wo**\<Installationsverzeichnis>** steht für das JasperServer-Installationsverzeichnis.
1.  Suchen Sie die**\<Installationsverzeichnis>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** Datei und fügen Sie die folgenden Zeilen hinzu:

**XML**

{{< highlight "csharp" >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **Überprüfen Sie, ob die Lizenz funktioniert**

Exportieren Sie einen beliebigen Bericht in das Format XLS und prüfen Sie, ob der Bericht eine Bewertungsmeldung enthält. Wenn keine Evaluierungsmeldung angezeigt wird, funktioniert die Lizenz ordnungsgemäß.

**Aspose.Cells for JasperReports fügt ein Bewertungsarbeitsblatt im Bewertungsmodus ein** 

![todo: Bild_alt_Text](licensing_1.png)

**Bei einer gültigen Lizenz gibt es kein Bewertungsarbeitsblatt** 

![todo: Bild_alt_Text](licensing_2.png)

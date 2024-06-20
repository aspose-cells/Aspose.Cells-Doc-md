---
title: Licensiering
type: docs
weight: 40
url: /sv/jasperreports/licensing/
---

{{% alert color="primary" %}}

Aspose.Cells for JasperReports finns som en gratis, tidsbegränsad utvärdering från [nedladdningssidan](https://downloads.aspose.com/cells/jasperreports). Utvärderings- och licensierade versioner av produkten är samma nedladdning.

När du är nöjd med utvärderingsversionen kan du [köpa en licens](https://purchase.aspose.com/). Se till att du förstår och samtycker till licensvillkoren.

Licensen är tillgänglig för nedladdning från beställningssidan när beställningen har betalats. Licensen är en tydlig text, digitalt signerad XML-fil. Licensen innehåller information som klientnamn, köpt produkt och licens typ. Ändra inte innehållet i licensfilen: att göra så ogiltigförklarar licensen.

Det finns två sätt att tillämpa en licens:

- [Anropa setLicense](/cells/sv/jasperreports/licensing/#call-setlicense)
- [Ange en exportparameter i applicationContext.xml](/cells/sv/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

Efter att ha installerat licensen,

- [Verifiera att den fungerar](/cells/sv/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **Anropa setLicense**

{{% alert color="primary" %}}

Denna metod är tillämplig för användning med JasperReports.

{{% /alert %}}

Ladda ned licensen till din dator och kopiera den till lämplig mapp (till exempel din applikationsmapp eller **JasperReports\lib**).
Lägg till följande kod i ditt projekt:

{{< highlight csharp >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **Ange licensfilens exportparameter i applicationContext.xml**

{{% alert color="primary" %}}

Denna metod är tillämplig för användning med JasperServer.

{{% /alert %}}

1. Download the license to your computer and copy it to the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF** folder, where **\<InstallDir>** stands for the JasperServer installation directory.
1. Locate the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** file and add the following lines:

**XML**

{{< highlight csharp >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **Verifiera att licensen fungerar**

Exportera en rapport till XLS-format och kontrollera om rapporten innehåller ett utvärderingsmeddelande. Om det inte finns något utvärderingsmeddelande fungerar licensen korrekt.

**Aspose.Cells for JasperReports infogar en utvärderingsarbetsblad i utvärderingsläge** 

![todo:image_alt_text](licensing_1.png)

**När en giltig licens finns finns det ingen utvärderingsarbetsblad** 

![todo:image_alt_text](licensing_2.png)

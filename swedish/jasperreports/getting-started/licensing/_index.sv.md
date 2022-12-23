---
title: Licensiering
type: docs
weight: 40
url: /sv/jasperreports/licensing/
---
{{% alert color="primary" %}}

 Aspose.Cells for JasperReports är tillgänglig som en gratis, obegränsad tidsbegränsad utvärdering från[nedladdningssida](https://downloads.aspose.com/cells/jasperreports). Utvärderingen och licensierade versioner av produkten är samma nedladdning.

 När du är nöjd med utvärderingsversionen kan du[köpa en licens](https://purchase.aspose.com/). Se till att du förstår och godkänner licensvillkoren.

Licensen finns tillgänglig för nedladdning från beställningssidan när beställningen är betald. Licensen är en klartext, digitalt signerad XML-fil. Licensen innehåller information som kundnamn, köpt produkt och licenstyp. Ändra inte innehållet i licensfilen: om du gör det ogiltigförklaras licensen.

Det finns två sätt att ansöka om en licens:

- [Ring setLicense](/cells/sv/jasperreports/licensing/#call-setlicense)
- [Ställ in en exportparameter i applicationContext.xml](/cells/sv/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

Efter installation av licensen,

- [Kontrollera att det fungerar](/cells/sv/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **Ring setLicense**

{{% alert color="primary" %}}

Denna metod är tillämplig för användning med JasperReports.

{{% /alert %}}

 Ladda ner licensen till din dator och kopiera den till lämplig mapp (till exempel din applikations mapp eller**JasperReports\lib**).
Lägg till följande kod till ditt projekt:

{{< highlight "csharp" >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **Ställ in parametern licenseFile Exporter i applicationContext.xml**

{{% alert color="primary" %}}

Denna metod är tillämplig för användning med JasperServer.

{{% /alert %}}

1.  Ladda ner licensen till din dator och kopiera den till**\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF**mapp, var**\<InstallDir>** står för installationskatalogen JasperServer.
1.  Leta upp**\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** fil och lägg till följande rader:

**XML**

{{< highlight "csharp" >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **Verifiera att licensen fungerar**

Exportera valfri rapport till formatet XLS och kontrollera om rapporten innehåller ett utvärderingsmeddelande. Om det inte finns något utvärderingsmeddelande, fungerar licensen korrekt.

**Aspose.Cells for JasperReports injicerar ett utvärderingsark i utvärderingsläge** 

![todo:image_alt_text](licensing_1.png)

**När en giltig licens finns det inget utvärderingsark** 

![todo:image_alt_text](licensing_2.png)

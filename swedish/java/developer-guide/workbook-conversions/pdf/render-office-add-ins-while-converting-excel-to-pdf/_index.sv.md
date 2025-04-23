---
title: Rendera Office tillägg vid konvertering av Excel till PDF
type: docs
weight: 90
url: /sv/java/render-office-add-ins-while-converting-excel-to-pdf/
---

## **Möjliga användningsscenario**
Tidigare kunde inte Aspose.Cells rendera Office-tillägg när Excel-filen sparades till PDF-format. Nu renderar Aspose.Cells det bra. Du behöver inte använda någon särskild metod eller egenskap för att rendera Office-tillägg i utdat-PDF. Spara bara din Excel-fil till PDF-format och den kommer att rendera Office-tillägg.
## **Rendera Office-tillägg vid konvertering av Excel till PDF**
Följande provkod sparar [prov-Excel-filen](60489783.xlsx) som innehåller Office-tilläggen. Se [utdata-PDF genererad med föregående version dvs. 17.11](60489781.pdf) och [utdata-PDF genererad med nyare version dvs. 17.12 och högre](60489782.pdf). Den tidigare versionen av utdata-PDF är tom men den nyare versionen av utdata-PDF visar Office-tillägget.
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-RenderOfficeAdd_InsWhileConvertingExcelToPdf.java" >}}
{{< app/cells/assistant language="java" >}}

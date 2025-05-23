---
title: Konvertera XLS fil med bilder eller diagram till PDF
type: docs
weight: 50
url: /sv/net/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells stödjer att konvertera XLS-filer som innehåller bilder och diagram till PDF-dokument. Aspose.Cells for .NET kan arbeta självständigt för att konvertera ett kalkylblad till PDF: Aspose.PDF för .NET krävs inte för konverteringen. Processen kan göras i minnet eftersom processen inte är beroende av temporära eller intermediära XML-filer. Detta innebär att stora Excel-filer, till exempel de som innehåller bilder, diagram och andra ritobjekt, kan konverteras snabbt och effektivt.

{{% /alert %}} 
## **Exempelkod**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}} 

Om kalkylarket innehåller formler är det bäst att anropa [Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)-metoden precis innan rendering till PDF. Genom att göra det säkerställs att formelberoende värden beräknas på nytt och korrekta värden renderas i PDF:n.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}

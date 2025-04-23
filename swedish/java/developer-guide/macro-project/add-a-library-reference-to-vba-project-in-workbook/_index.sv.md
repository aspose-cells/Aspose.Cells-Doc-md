---
title: Lägg till en biblioteksreferens till VBA projekt i arbetsbok
type: docs
weight: 10
url: /sv/java/add-a-library-reference-to-vba-project-in-workbook/
description: Lär dig hur du lägger till en biblioteksreferens till VBA projektet i arbetsboken med hjälp av Aspose.Cells for Java API.
keywords: Hur man lägger till en biblioteksreferens till VBA projektet i arbetsboken i Java, Infoga en biblioteksreferens till VBA projektet i arbetsboken med Java, Java Ange biblioteksreferens till VBA projektet i arbetsboken. 
---

{{% alert color="primary" %}}

I Microsoft Excel kan du lägga till en biblioteksreferens till VBA-projektet genom att klicka på **Verktyg > Referenser...** manuellt. Det kommer att öppna följande dialogruta som hjälper dig att välja från befintliga referenser eller bläddra igenom ditt bibliotek själv.

![todo:image_alt_text](add-a-library-reference-to-vba-project-in-workbook_1.png)

Men ibland behöver du lägga till eller registrera biblioteksreferensen till VBA-projektet genom kod. Du kan göra det med hjälp av Aspose.Cells [**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference-java.lang.String-java.lang.String-) metod.

{{% /alert %}}

## **Hur man lägger till en biblioteksreferens till VBA-projektet i arbetsboken**

Följande exempelkod lägger till eller registrerar två biblioteksreferenser till VBA-projektet för arbetsboken med hjälp av [**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference-java.lang.String-java.lang.String-) -metoden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
{{< app/cells/assistant language="java" >}}

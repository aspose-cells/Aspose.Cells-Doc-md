---
title: Lägg till en biblioteksreferens till VBA-projektet i arbetsboken
type: docs
weight: 10
url: /sv/java/add-a-library-reference-to-vba-project-in-workbook/
---
{{% alert color="primary" %}}

 I Microsoft Excel kan du lägga till en biblioteksreferens till VBA-projektet genom att klicka på**Verktyg > Referenser...** manuellt. Den öppnar följande dialogruta som hjälper dig att välja från befintliga referenser eller bläddra i ditt bibliotek själv.

![todo:image_alt_text](add-a-library-reference-to-vba-project-in-workbook_1.png)

 Men ibland måste du lägga till eller registrera biblioteksreferensen till VBA-projektet genom kod. Du kan göra det med Aspose.Cells[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) metod.

{{% /alert %}}

## **Lägg till en biblioteksreferens till VBA-projektet i arbetsboken**

 Följande exempelkod lägger till eller registrerar två biblioteksreferenser till VBA-projektet för arbetsboken som använder[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}

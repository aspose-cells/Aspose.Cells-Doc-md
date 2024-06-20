---
title: Tillgång till textfältet genom namnet
type: docs
weight: 580
url: /sv/java/access-the-text-box-by-the-name/
---

{{% alert color="primary" %}} 

Tidigare har textfält åtkomsts genom index från [Workheet.getTextBoxes()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes) samlingen men nu kan du också åtkomma textfältet genom namn från denna samling. Detta är ett bekvämt och snabbt sätt att få åtkomst till ditt textfält om du redan känner till dess namn.

{{% /alert %}} 
## **Tillgång till textfältet genom namnet**
Följande provkod skapar först en textruta och tilldelar den någon text och namn. Sedan i de följande raderna får vi åtkomst till samma textruta genom dess namn och skriver ut dess text.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessTextBoxName-AccessTextBoxName.java" >}}
## **Konsoloutput**
Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

 This is MyTextBox

{{< /highlight >}}

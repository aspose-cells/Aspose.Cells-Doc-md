---
title: Tillgång till textfältet genom namnet
type: docs
weight: 230
url: /sv/net/access-the-text-box-by-the-name/
---

## Åtkomst till textlådan med namnet

Tidigare fick man åtkomst till textboxar med index från [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes) samlingen men nu kan du också få åtkomst till textboxen med namn från denna samling. Detta är ett bekvämt och snabbt sätt att få åtkomst till din textruta om du redan känner till dess namn.

Följande provkod skapar först en textruta och tilldelar den någon text och namn. Sedan i de följande raderna får vi åtkomst till samma textruta genom dess namn och skriver ut dess text.

### C#-kod för att få åtkomst till textlådan med namn

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AccessTextBoxName-AccessTextBoxName.cs" >}}

### Konsoloutput som genereras av provkoden

Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}

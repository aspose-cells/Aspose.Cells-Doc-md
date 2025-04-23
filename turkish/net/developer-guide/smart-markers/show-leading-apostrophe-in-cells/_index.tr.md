---
title: Hücrelerde öncü apostrofu gösterme
type: docs
weight: 70
url: /tr/net/show-leading-apostrophe-in-cells/
---

Microsoft Excel'de hücre değerindeki öncü apostrof gizlenir. Aspose.Cells, önceden apostrofu varsayılan olarak gösterme özelliği sağlar. Bu amaçla, API [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) özelliğini sağlar. Bu özellik, tek tırnakla başlayan dize değerini hücreye girerken [QuotePrefix](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) özelliğini ayarlayıp ayarlamayacağını belirtir. [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) özelliğini **false** olarak ayarlamak, çıkış excel dosyasında öncü apostrofu görüntüler.

Aşağıdaki ekran görüntüsü, çıkış excel dosyasını görünen öncü apostrofla göstermektedir.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

Aşağıdaki kod parçası, kaynak excel dosyasına Akıllı İmlerle veri ekleyerek bunu gösterir. Kaynak ve çıkış excel dosyaları referans için ekte verilmiştir.

[Kaynak Dosya](98107425.xlsx)

[Çıkış Dosyası](98107426.xlsx)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

*DataObject* sınıfının uygulaması aşağıda verilmiştir

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
{{< app/cells/assistant language="csharp" >}}

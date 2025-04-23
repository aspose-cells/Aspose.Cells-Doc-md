---
title: Veri Tablolarının Dizilerini Hesaplama
type: docs
weight: 550
url: /tr/java/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}} 

Microsoft Excel'de Veri > What-If Analizi > Veri Tablosu... kullanarak Veri Tablosu oluşturabilirsiniz. Artık Aspose.Cells ile veri tablosunun dizi formülü hesaplanabilir. Herhangi bir formül türünü hesaplamak için [Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) yöntemi normal şekilde kullanılabilir.

{{% /alert %}} 
## **Veri Tablolarının Dizi Formül Hesaplama**
Aşağıdaki örnek kodda, [kaynak excel dosyasını](5472579.xlsx) kullandık, bu dosya ayrıca aşağıdaki resimde gösterilmiştir.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

Eğer B1 hücresinin değerini 100 olarak değiştirirseniz, Sarı renk ile doldurulan Veri Tablosundaki değerler 120 olacaktır. Örnek kod, 120 olarak Veri Tablosundaki değerleri gösteren [çıktı PDF'yi](5472577.pdf) oluşturur, bu da bu resimde gösterildiğidir.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

İşte [çıktı PDF'yi](5472577.pdf) [kaynak excel dosyasından](5472579.xlsx) üretmek için kullanılan örnek kod. Daha fazla bilgi için yorumları okuyun.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
{{< app/cells/assistant language="java" >}}

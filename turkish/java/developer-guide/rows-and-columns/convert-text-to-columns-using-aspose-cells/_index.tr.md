---
title: Aspose.Cells Kullanarak Metni Sütunlara Dönüştürme
type: docs
weight: 70
url: /tr/java/convert-text-to-columns-using-aspose-cells/
---

## **Olası Kullanım Senaryoları**
Microsoft Excel kullanarak metninizi Sütunlara çevirebilirsiniz. Bu özellik, *Data Tools* altındaki *Data* sekmesinde bulunur. Bir sütunun içeriğini çoklu sütunlara ayırmak için, verilerin belirli bir ayırıcı içermesi gerekir, örneğin bir virgül (veya başka herhangi bir karakter), buna göre Microsoft Excel hücre içeriğini birden fazla hücreye ayırır. Aspose.Cells, bu özelliği [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) metodu ile de sağlar.
## **Aspose.Cells Kullanarak Metni Sütunlara Dönüştürme**
Aşağıdaki örnek kod, [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) metodunun kullanımını açıklar. Kod önce ilk çalışma sayfasındaki A sütununa bazı isimler ekler. Ad ve soyad boşluk karakteri ile ayrılmıştır. Daha sonra A sütunundaki hücreye [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) metodunu uygular ve sonucu bir çıktı excel dosyası olarak kaydeder. Eğer [çıktı excel dosyasını](25395230.xlsx) açarsanız, ilk isimlerin A sütununda, soy isimlerin ise B sütununda olduğunu göreceksiniz ki, bu da ekran görüntüsüyle gösterilmiştir.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
{{< app/cells/assistant language="java" >}}

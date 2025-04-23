---
title: Excel dosyasında Saklanacak Önemli Basamakların Belirtilmesi
type: docs
weight: 20
url: /tr/java/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **Olası Kullanım Senaryoları**

Varsayılan olarak, Aspose.Cells, elektronik tabloların içindeki çift değerlerin 17 önemli basamağını depolar; Excel uygulaması ise yalnızca 15 önemli basamağını depolar. Aspose.Cells'in bu durumda varsayılan davranışını değiştirebilirsiniz; yani, [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits) özelliğini kullanarak 17'den 15 önemli basamağa değiştirebilirsiniz.

## **Excel dosyasında Saklanacak Önemli Basamakların Belirtilmesi**

Aşağıdaki örnek kod, Aspose.Cells'in excel dosyasının içine çift değerleri saklarken 15 önemli basamağı kullanmasını zorlamaktadır. Lütfen [çıktı excel dosyası](23166982.xlsx)'nı kontrol edin. Uzantısını .zip olarak değiştirin ve açın, 15 önemli basamağın sadece excel dosyasının içine saklandığını göreceksiniz. Aşağıdaki ekran görüntüsü, [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits) özelliğinin çıktı excel dosyası üzerindeki etkisini açıklamaktadır.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
{{< app/cells/assistant language="java" >}}

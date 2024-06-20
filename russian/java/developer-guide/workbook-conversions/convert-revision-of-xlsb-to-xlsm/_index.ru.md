---
title: Преобразование ревизии из XLSB в XLSM
type: docs
weight: 2200
url: /ru/java/convert-revision-of-xlsb-to-xlsm/
---

{{% alert color="primary" %}} 

Aspose.Cells теперь поддерживает полное преобразование ревизий файла XLSB в файл XLSM. Ревизии находятся внутри пути \xl\revisions. Вы можете просмотреть их, изменив расширение файла XLSB на ZIP. В папке \xl\revisions находятся файлы с расширением .bin.

При преобразовании файла XLSB в файл XLSM с помощью Aspose.Cells эти файлы .bin успешно преобразуются в файлы .xml, как показано на этих двух скриншотах.

{{% /alert %}} 
## **Преобразование версии XLSB в XLSM**
На следующем скриншоте показаны файлы .bin в папке \xl\revisions файла XLSB.

![todo:image_alt_text](convert-revision-of-xlsb-to-xlsm_1.png)

На следующем скриншоте показано, как файлы .bin были преобразованы в файлы .xml при преобразовании файла XLSB в формат XLSM с использованием Aspose.Cells.

![todo:image_alt_text](convert-revision-of-xlsb-to-xlsm_2.png)

Вот код для преобразования файла XLSB в формат XLSM с использованием Aspose.Cells.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertRevisionOfXLSBtoXLSM-ConvertRevisionOfXLSBtoXLSM.java" >}}

---  
title: Satır Sonları ve Metin Kaydırma
linktitle: Satır Sonları ve Metin Kaydırma  
description: Node.js de C++ kullanarak Aspose.Cells kütüphanesiyle metin sarmalama ve kelime sarması nasıl uygulanır. Aspose.Cells kütüphanesini kullanarak hücrelere metin kolayca ekleyebilir ve manuel kelime sarması, kelime sarması gibi metin sarmalama yöntemlerini ayarlayabilirsiniz. Bu belge, bu özelliklerin nasıl uygulanacağını detaylandırmakta ve örnek kodlar sunmaktadır.  
keywords: Aspose.Cells, satır sonları, metin kaydırma, metin düzeni Node.js via C++  
type: docs  
weight: 60  
url: /tr/nodejs-cpp/line-breaks-and-text-wrapping/  
---  

{{% alert color="primary" %}}  
Hücredeki metnin okunabilmesi için, açık satır sonları ve metin kaydırma uygulanabilir. Metin kaydırma, hücredeki bir satırı birden fazla satıra dönüştürür, açık satır sonları istediğiniz yerde kesmek için kullanılır.  
{{% /alert %}}  

## **Hücrede Metin Kaydırma**  
Bir hücrede metin sarmak için, [**Aspose.Cells.Style.setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-) metodunu kullanın.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapTextInCell.js" >}}


## **Açık Satır Sonları Kullanımı**  
JavaScript'te, hücreye net satır sonları eklemek için '\n' kullanabilirsiniz.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-UseExplicitLineBreaks.js" >}}



{{< app/cells/assistant language="nodejs-cpp" >}}

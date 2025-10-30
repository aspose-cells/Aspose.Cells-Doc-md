---  
title: Orijinal Değerler Kullanarak Veri Arama
type: docs  
weight: 380  
url: /tr/nodejs-cpp/search-data-using-original-values/  
description: Orijinal Değerleri kullanarak Veri Arama nasıl yapılır öğrenin, Aspose.Cells for Node.js via C++ API si aracılığıyla.  
keywords: Orijinal Değerleri kullanarak Veri Arama Node.js üzerinden C++ ile, Orijinal Değerleri kullanarak Veri Bulma Node.js üzerinden C++, Orijinal Değerlerle Veri Arama Node.js üzerinden C++, Orijinal Değerlerle Veri Bulma Node.js üzerinden C++  
---  

{{% alert color="primary" %}}  

Bazen verinin değeri bazı şekilde biçimlendirildiği için gizlidir. Örneğin, D4 hücresinin değeri =Sum(A1:A2) ve değeri 20'dir ancak --- olarak biçimlendirilmiştir, bu nedenle 20 değeri gizlidir ve Microsoft Excel bulma seçenekleri kullanılarak bulunamaz. Bununla birlikte, Aspose.Cells kullanarak [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype) kullanarak bulunabilir.  

{{% /alert %}}  

Aşağıdaki örnek kod yukarıdaki noktayı açıklar. Microsoft Excel bulma seçenekleri kullanılarak bulunamayan D4 hücresini [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype) kullanarak bulur ancak Aspose.Cells kullanarak bulabilir. Daha fazla bilgi için kod içindeki yorumları okuyun.  

## Node.js kodu ile orijinal değerleri kullanarak veri arama  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchDataUsingOriginalValues.js" >}}


## Örnek Kod Tarafından Oluşturulan Konsol Çıktısı  

Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.  

{{< highlight java >}}  

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}

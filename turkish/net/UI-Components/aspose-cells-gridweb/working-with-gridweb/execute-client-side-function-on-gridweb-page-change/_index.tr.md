---
title: GridWeb sayfa değişikliğinde istemci tarafı işlevini yürütün
type: docs
weight: 140
url: /tr/net/execute-client-side-function-on-gridweb-page-change/
---
## **Olası Kullanım Senaryoları**
Bazen, GridWeb sayfası değiştiğinde müşteri tarafı işlevinizi yürütmeniz gerekir. Aspose.Cells.GridWeb, bu amaçla OnPageChangeClientFunction özelliğini sağlar. Lütfen bu özelliği, yürütmek istediğiniz istemci tarafı işleviyle ayarlayın.
## **GridWeb sayfa değişikliğinde istemci tarafı işlevini yürütün**
Aşağıdaki aspx biçimlendirmesi, OnPageChangeClientFunction özelliğinin nasıl kullanılacağını açıklar. Özelliği, MyOnPageChange adlı istemci tarafı işleviyle ayarlar. Lütfen unutmayın, bu özellik yalnızca sayfalamayı etkinleştirdiyseniz geçerlidir, yani EnablePaging="true". Şimdi, GridWeb sayfasını ne zaman değiştirirseniz, istemci tarafı işlevi MyOnPageChange'i çağıracaktır.**geçerli sayfa dizini** üzerinde**konsol** bu ekran görüntüsünde gösterildiği gibi.

![yapılacaklar:resim_alternatif_Metin](execute-client-side-function-on-gridweb-page-change_1.png)
## **Basit kod**
Bu, GridWeb'de OnPageChangeClientFunction="MyOnPageChange" özelliğinin ayarlanması nedeniyle yürütülecek istemci tarafı işlevi MyOnPageChange'in kodudur. Bu, tam aspx sayfa işaretlemesidir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}

---
title: GridWeb sayfa değişikliğinde istemci tarafı fonksiyonunu yürütme
type: docs
weight: 140
url: /tr/net/aspose-cells-gridweb/execute-client-side-function-on-gridweb-page-change/
keywords: GridWeb,client,js,javascript,function
description: Bu makale, GridWeb deki istemci js fonksiyonu ile nasıl çalışılacağını tanıtıyor.
---

## **Olası Kullanım Senaryoları**
Bazen GridWeb sayfa değiştiğinde istemci tarafı fonksiyonunuzu yürütmek isteyebilirsiniz. Aspose.Cells.GridWeb, bunun amacıyla OnPageChangeClientFunction özelliğini sağlar. Lütfen bu özelliği istemci tarafı fonksiyonunuzla ayarlayın bu özelliği yürütmek istediğiniz.
## **GridWeb sayfa değişikliğinde istemci tarafı fonksiyonunu yürütme**
Aşağıda açıklanan aspx işareti, OnPageChangeClientFunction özelliğinin nasıl kullanılacağını açıklıyor. Bu özelliği, MyOnPageChange adlı istemci tarafı fonksiyonuyla ayarlar. Lütfen unutmayın, bu özellik yalnızca sayfalama etkinleştirilmişse geçerlidir, yani EnablePaging="true". Şimdi, GridWeb sayfasını değiştirdiğinizde, **konsolda** gösterildiği gibi **mevcut sayfa dizinini** yazdıran MyOnPageChange istemci tarafı fonksiyonunu çağıracaktır.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Örnek Kod**
GridWeb'de OnPageChangeClientFunction ="MyOnPageChange" özelliğini ayarladığınız için yürütülecek istemci tarafı fonksiyon MyOnPageChange kodu. Bu tam aspx sayfa işareti.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}

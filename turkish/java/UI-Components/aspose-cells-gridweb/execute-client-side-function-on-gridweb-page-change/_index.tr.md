---
title: GridWeb sayfası değişikliğinde istemci tarafı işlevini yürütün
type: docs
weight: 70
url: /tr/java/execute-client-side-function-on-gridweb-page-change/
---
##  **Olası Kullanım Senaryoları**
Bazen GridWeb sayfası değiştiğinde istemci tarafı işlevinizi yürütmeniz gerekir. Aspose.Cells.GridWeb, bu amaç için OnPageChangeClientFunction özelliğini sağlar. Lütfen bu özelliği, yürütmek istediğiniz istemci tarafı işleviyle ayarlayın.
##  **GridWeb sayfası değişikliğinde istemci tarafı işlevini yürütün**
 Aşağıdaki Java kodu GridWebBean.setOnPageChangeClientFunction() özelliğinin nasıl kullanılacağını açıklamaktadır. Özelliği MyOnPageChange adlı istemci tarafı işleviyle ayarlar. Lütfen bu özelliğin yalnızca sayfalamayı etkinleştirdiyseniz, yani GridWebBean.setEnablePaging(true) geçerli olduğunu unutmayın. Artık GridWeb sayfasını değiştirdiğinizde, istemci tarafı işlevi MyOnPageChange'i çağıracak ve bu işlev aşağıdakileri yazdıracaktır:**geçerli sayfa dizini** üzerinde**konsol** bu ekran görüntüsünde gösterildiği gibi.

![yapılacak şey:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
##  **Basit kod**
Bu, bu satır nedeniyle yürütülecek olan istemci tarafı işlevi MyOnPageChange'in kodudur, yani Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight "java" >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

Aşağıdaki kod, sayfalamanın nasıl etkinleştirileceğini ve OnPageChangeClientFunction özelliğinin nasıl ayarlanacağını açıklamaktadır.

{{< highlight "java" >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}

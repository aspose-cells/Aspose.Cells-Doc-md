---
title: Определение, защищен ли проект VBA
type: docs
weight: 80
url: /ru/java/find-out-if-vba-project-is-protected/
---

## **Возможные сценарии использования**
Вы можете узнать, защищен ли проект VBA (Visual Basic Applications) вашего файла Excel или нет с помощью Aspose.Cells, используя метод [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected)
## **Образец кода**
В следующем примере кода создается книга, а затем проверяется, защищен ли ее проект VBA или нет. Затем проект VBA защищается, и снова проверяется, защищен ли его проект VBA или нет. Пожалуйста, обратитесь к его консольному выводу для справки. До защиты [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) возвращает **false**, но после защиты он возвращает **true**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **Вывод в консоль**
Это вывод консоли приведенного выше образца кода для справки.

{{< highlight java >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

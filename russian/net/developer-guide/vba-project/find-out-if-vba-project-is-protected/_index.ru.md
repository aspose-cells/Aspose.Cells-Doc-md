---
title: Определение, защищен ли проект VBA
type: docs
weight: 20
url: /ru/net/find-out-if-vba-project-is-protected/
---

## **Определение, защищен ли проект VBA на C#**

Вы можете узнать, защищен ли проект VBA (Visual Basic Applications) вашего файла Excel или нет с помощью свойства [**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) в Aspose.Cells.

## **Образец кода**

Приведенный ниже образец кода создает книгу, затем проверяет, защищен ли ее проект VBA или нет. Затем он защищает проект VBA и снова проверяет, защищен ли его проект VBA или нет. Пожалуйста, ознакомьтесь с выводом консоли для справки. До защиты [**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) возвращает **false**, но после защиты оно возвращает **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-FindoutifVBAProjectisProtected.cs" >}}

## **Вывод в консоль**

Это вывод консоли приведенного выше образца кода для справки.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

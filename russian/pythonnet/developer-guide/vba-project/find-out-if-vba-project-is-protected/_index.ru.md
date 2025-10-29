---
title: Определение, защищен ли проект VBA
type: docs
weight: 20
url: /ru/python-net/find-out-if-vba-project-is-protected/
---

## **Узнайте, защищен ли VBA-проект в Python**

Вы можете определить, защищен ли VBA (Visual Basic Applications) проект вашего файла Excel или нет с помощью Aspose.Cells для Python via .NET и свойства [**VbaProject.is_protected**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_protected).

## **Образец кода**

Приведенный ниже образец кода создает книгу, затем проверяет, защищен ли ее проект VBA или нет. Затем он защищает проект VBA и снова проверяет, защищен ли его проект VBA или нет. Пожалуйста, ознакомьтесь с выводом консоли для справки. До защиты [**VbaProject.is_protected**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_protected) возвращает **false**, но после защиты оно возвращает **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FindoutifVBAProjectisProtected.py" >}}

## **Вывод в консоль**

Это вывод консоли приведенного выше образца кода для справки.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}

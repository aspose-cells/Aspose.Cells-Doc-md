---
title: Узнайте, защищен ли проект VBA
type: docs
weight: 80
url: /ru/java/find-out-if-vba-project-is-protected/
---
## **Возможные сценарии использования**
 Вы можете узнать, защищен ли проект VBA (Visual Basic Applications) вашего файла Excel с помощью Aspose.Cells, используя[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected)метод
## **Образец кода**
Следующий пример кода создает книгу, а затем проверяет, защищен ли ее проект VBA. Затем он защищает проект VBA и снова проверяет, защищен ли его проект VBA или нет. См. его консольный вывод для справки. Перед защитой,[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) возвращается**ЛОЖЬ** но после защиты возвращается**истинный**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **Консольный вывод**
Это консольный вывод приведенного выше примера кода для справки.

{{< highlight "java" >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}

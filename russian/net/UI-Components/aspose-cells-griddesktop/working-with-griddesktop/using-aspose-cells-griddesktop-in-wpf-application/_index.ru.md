---
title: Использование элемента управления Aspose.Cells.GridDesktop в приложении WPF
type: docs
weight: 50
url: /ru/net/aspose-cells-griddesktop/use-aspose-cells-griddesktop-in-wpf-application/
keywords: GridDesktop,wpf
description: Эта статья рассказывает, как использовать GridDesktop в приложении WPF.
---

{{% alert color="primary" %}} 

В этой статье демонстрируется, как использовать конструктор приложений Windows Presentation Foundation (WPF) для Visual Studio для размещения элемента управления Windows Forms, такого как Aspose.Cells.GridDesktop, в приложении WPF. 
Мы будем использовать Visual Studio 2015 для демонстрации процесса, однако вы можете использовать любую версию, включая Visual Studio 2008 или более поздние.

{{% /alert %}} 

Этот учебник проведет вас через процесс добавления элемента управления Aspose.Cells.GridDesktop в приложение WPF. Вам понадобится любая версия среды разработки Visual Studio, которая поддерживает разработку WPF, чтобы попробовать это на своей стороне.
## **Создайте приложение WPF с использованием Visual Studio**
Сначала создайте приложение WPF, используя среду разработки Visual Studio. Щелкните по меню **Файл** >> **Новый** >> **Проект** и выберите **Приложение WPF** из шаблонов, дайте проекту имя и нажмите **OK**. Вы можете ориентировать свой проект на любой .NET Framework выше 2.0, однако вы не можете использовать клиентские профили .NET Frameworks.
## **Добавьте ссылки на необходимые пространства имен.**
Добавьте ссылки на следующие сборки,щелкнув правой кнопкой мыши ссылки в окне обозревателя решений и выбрав меню Добавить ссылку.

- Сборка WindowsFormsIntegration (WindowsFormsIntegration.dll).
- Сборка Windows Forms (System.Windows.Forms.dll).
- Сборка Aspose.Cells.GridDesktop (Aspose.Cells.GridDesktop.dll).

Это действие добавляет необходимые сборки в приложение, копирует их в папку Bin приложения.
## **Добавьте ссылки на XAML.**
Затем перейдите к файлу XAML и добавьте следующие пространства имен и ссылки на сборки внутри тега Windows.

{{< highlight java >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**Финальный тег Windows будет выглядеть примерно так, как показано ниже.**

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **Добавьте элемент управления Aspose.Cells.GridDesktop в XAML.**
Просто добавьте следующий код внутрь тега Grid в XAML. Тег **WindowsFormsHost** используется для размещения элемента управления Windows Forms, а тег **gridDesktop:GridDesktop** представляет элемент управления Aspose.Cells.GridDesktop. Вы также можете назвать элемент управления, чтобы его можно было легко ссылаться в коде.

{{< highlight java >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**Финальное XAML будет выглядеть следующим образом.** 

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Используйте Aspose.Cells.GridDesktop.**
Теперь мы можем получить доступ и использовать элемент управления Aspose.Cells.GridDesktop в файле .cs так же, как любые другие приложения Windows Forms. Для демонстрации простоты мы просто загружаем образец электронной таблицы в элемент управления Aspose.Cells.GridDesktop и сохраняем его обратно. Более того, мы использовали событие FrameworkElement_OnLoaded для запуска следующих операторов.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **Соберите и запустите.**
Теперь соберите и запустите приложение, используя **F5** или кнопку **Запуск** на пользовательском интерфейсе Visual Studio.

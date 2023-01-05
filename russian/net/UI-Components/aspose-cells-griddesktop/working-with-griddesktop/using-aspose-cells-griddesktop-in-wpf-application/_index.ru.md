---
title: Использование Aspose.Cells.GridDesktop в приложении WPF
type: docs
weight: 50
url: /ru/net/using-aspose-cells-griddesktop-in-wpf-application/
---
{{% alert color="primary" %}} 

 В этой статье показано, как использовать конструктор Presentation Foundation (WPF) Windows для Visual Studio для размещения элемента управления Forms Windows, такого как Aspose.Cells.GridDesktop, в приложении WPF.
Мы будем использовать Visual Studio 2015 для демонстрации процесса, однако вы можете использовать любую версию, включая Visual Studio 2008 или более позднюю версию.

{{% /alert %}} 

В этом руководстве описан процесс добавления элемента управления Aspose.Cells.GridDesktop в приложение WPF. Вам понадобится любая версия Visual Studio IDE, которая поддерживает разработку WPF, чтобы попробовать это на своей стороне.
## **Создайте приложение WPF с помощью Visual Studio.**
 Сначала создайте приложение WPF с помощью Visual Studio IDE. Нажмите на**Файл** >> **Новый** >> **Проект** меню и выберите**WPF-приложение** из Templates, назовите проект и нажмите**ХОРОШО**. Вы можете нацелить свой проект на любую платформу .NET выше 2.0, однако вы не можете использовать клиентский профиль .NET Frameworks.
## **Добавьте ссылки на необходимые пространства имен**
Добавьте ссылки на следующие сборки, щелкнув правой кнопкой мыши окно «Ссылки в обозревателе решений» и выбрав меню «Добавить ссылку».

- Сборка WindowsFormsIntegration (WindowsFormsIntegration.dll).
- Windows Сборка форм (System.Windows.Forms.dll).
- Aspose.Cells.Сборка GridDesktop (Aspose.Cells.GridDesktop.dll).

Это действие добавляет в приложение необходимые сборки, т.е. копирует сборки в папку Bin приложения.
## **Добавьте ссылки на XAML**
Затем перейдите к файлу XAML и добавьте следующие пространства имен и ссылки на сборки в теге Windows.

{{< highlight "java" >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**Окончательный тег Windows будет выглядеть так, как показано ниже.**

![дело:изображение_альтернативный_текст](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **Добавьте элемент управления Aspose.Cells.GridDesktop в XAML.**
 Просто добавьте приведенный ниже код внутрь тега Grid в XAML.**WindowsFormsHost** Тег используется для размещения Windows управления формами и**гриддесктоп: гриддесктоп** представляет элемент управления Aspose.Cells.GridDesktop. Вы также можете назвать элемент управления, чтобы на него можно было легко ссылаться в коде.

{{< highlight "java" >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**Окончательный XAML будет выглядеть следующим образом.** 

![дело:изображение_альтернативный_текст](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Используйте Aspose.Cells.GridDesktop**
Теперь мы можем получить доступ и использовать элемент управления Aspose.Cells.GridDesktop в файле .cs, как и любые другие приложения Windows Forms. Чтобы не усложнять демонстрацию, мы просто загружаем образец электронной таблицы в элемент управления Aspose.Cells.GridDesktop и сохраняем его обратно. Кроме того, мы использовали событие FrameworkElement_OnLoaded для запуска следующих операторов.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **Построить и запустить**
 Теперь создайте и запустите приложение, используя**F5** или же**Начинать** кнопку в пользовательском интерфейсе Visual Studio.

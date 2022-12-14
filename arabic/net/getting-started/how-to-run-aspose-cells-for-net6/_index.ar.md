---
title: كيفية تشغيل Aspose.Cells لـ NET6
type: docs
description: كيفية تشغيل Aspose.Cells لـ NET6
weight: 138
url: /ar/net/how-to-run-aspose-cells-for-net6/
---
## ملخص

 بالنسبة للأنظمة الأساسية .NET6 (أو الأحدث) ، قارن مع الأنظمة الأساسية السابقة (.netcore31 أو ما قبله) ، هناك فرق مهم يتعلق بمكتبة الرسومات.
 في هذا المسؤول[وثيقة Microsoft](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only)، فإنه يشرح لـ .NET6 أو الإصدارات الأحدث لمكتبة الرسومات "System.Drawing.Common" سيكون مدعومًا فقط على Windows ، ويقدم توصيات لاستبدال مكتبة الرسومات.

بالنسبة لمنتج Apose.Cells ، أجرينا التقييم وأكملنا ترحيل مكتبة الرسومات. نستخدم SkiaSharp بدلاً من System.Drawing.Common في الأنظمة غير Windows ، كما هو مقترح في الوثائق الرسمية لـ Microsoft. يرجى ملاحظة أن هذا التغيير الهام سوف يسري في Aspose.Cells 22.10.1 أو ما بعده لـ .Net6.

بالنسبة إلى .netcore31 أو ما قبله ، من أجل التوافق والاستقرار ، ما زلنا نستخدم حاليًا مكتبة الرسومات "System.Drawing.Common". التبعيات لـ netcore31 أو ما قبلها هي كما يلي:
- System.Drawing.Common ، 4.7.0.
- System.Security.Cryptography.Pkcs، 5.0.1.
- System.Text.Encoding.CodePages، 4.7.0.

## قم بتشغيل Aspose.Cells لـ .Net6 على Windows

يمكنك أولاً إنشاء تطبيق .net6 باستخدام VS2022 ، ثم يمكنك اختيار خيارات التثبيت التالية:

### قم بالتثبيت من خلال nuget

1.  ابحث عن Aspose.Cells من NuGet:[Aspose.Cells for .NET NuGet الحزمة](https://www.nuget.org/packages/Aspose.Cells/). 
يمكنك أيضًا تثبيت Aspose.Cells من مدير الحزم Nuget في VS2022.

2. سيتم تثبيت "SkiaSharp" أو "System.Drawing.Common" تلقائيًا كعنصر تبعية لـ Aspose.Cells 22.10.1 أو ما بعده لمنصات .Net6 ، والتي تعتمد على تكوين "Target OS" في مشروعك.
- اضبط "Target OS" على "Windows" لمشروعك ، ستستخدم "System.Drawing.Common" كاعتماد على نظام windows الخاص بك لمشروع NET6. في هذا التكوين ، تكون نتيجة الرسم أقرب إلى .netcore31 أو قبله.
**! [تكوين نظام التشغيل الهدف] (TargetOS.png)**
- عيّن "Target OS" إلى "None" أو خيارات أخرى لمشروعك ، ستستخدم "SkiaSharp" كاعتماد على نظام windows الخاص بك لمشروع .Net6. يرجى ملاحظة أن SkiaSharp لا يدعم حاليًا تنسيقات مثل EMF في Windows.

### التثبيت من خلال msi أو DLL

1. [قم بتنزيل Aspose.Cells.msi أو DLL](https://releases.aspose.com/cells/net/)

2. افتح دليل التثبيت أو دليل DLL ، ثم حدد الخطوة 3 أو 4 أدناه:

3. حدد موقع الدليل الفرعي "net6.0-windows" ، أضف Aspose.Cells.dll فيه إلى تطبيق net6 الخاص بك. أضف حزم nuget التالية يدويًا إلى مشروع .net6 الخاص بك:
- System.Drawing.Common ، 4.7.0.
- System.Security.Cryptography.Pkcs، 6.0.1.
- System.Text.Encoding.CodePages، 4.7.0.

بهذه الطريقة ، ستستخدم "System.Drawing.Common" كاعتماد على نظام windows الخاص بك لمشروع NET6. في هذا التكوين ، تكون نتيجة الرسم أقرب إلى .netcore31 أو قبله.

4. حدد موقع الدليل الفرعي "net6.0" ، أضف Aspose.Cells.dll فيه إلى تطبيق net6 الخاص بك. أضف حزم nuget التالية يدويًا إلى مشروع .net6 الخاص بك:
- SkiaSharp ، 2.88.3.
- System.Security.Cryptography.Pkcs، 6.0.1.
- System.Text.Encoding.CodePages، 4.7.0.

بهذه الطريقة ، سوف تستخدم "SkiaSharp" كإعتماد على نظام windows الخاص بك لمشروع .Net6. يرجى ملاحظة أن SkiaSharp لا يدعم حاليًا تنسيقات مثل EMF في Windows.

## قم بتشغيل Aspose.Cells لـ .Net6 على Linux

راجع طريقة التثبيت على Windows ، يمكنك فقط تحديد SkiaSharp كمكتبة رسومات تعتمد على نظام Linux.

تحتاج إلى القيام بالعمليات الإضافية التالية لضمان الاستخدام المناسب لـ SkiaSharp في نظام Linux:

1. قم بتشغيل الأمر التالي في نظام Linux الخاص بك:
```
apt-get update && apt-get install -y libfontconfig1
```
أو
```
apk update && apk add fontconfig 
```

2. أضف حزم nuget "SkiaSharp.NativeAssets.Linux 2.88.3" لمشروع net6 الخاص بك.

3. أو يمكنك اختيار إضافة حزمة nuget "SkiaSharp.NativeAssets.Linux.NoDependencies 2.88.3" إلى مشروع net6 الخاص بك ، بدلاً من الخطوتين المذكورتين أعلاه.

### مثال Dockerfile لأوبونتو

1. أضف حزم nuget "SkiaSharp.NativeAssets.Linux 2.88.3" إلى مشروع net6 الخاص بك.

2. استخدم Dockerfile التالي:
{{< highlight "plain" >}}
# Ubuntu 20.04
FROM mcr.microsoft.com/dotnet/runtime:6.0-focal AS base
WORKDIR /app

# add "libfontconfig1" package if using "SkiaSharp.NativeAssets.Linux" in your project
# Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apt-get update && apt-get install -y libfontconfig1

# Copy fonts from local to docker
# For example, put a "fonts" folder in your project folder, and put the font files in it,
# then, use the following line:
COPY fonts/ /usr/share/fonts

FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build
WORKDIR /src
COPY ["Ubuntu_Docker.csproj", "."]RUN dotnet restore "./Ubuntu_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Ubuntu_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ubuntu_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ubuntu_Docker.dll"]{{< /highlight >}}

### مثال Dockerfile لجبال الألب

1. أضف حزم nuget "SkiaSharp.NativeAssets.Linux 2.88.3" إلى مشروع net6 الخاص بك.

2. استخدم Dockerfile التالي:
{{< highlight "plain" >}}
# Alpine 3.16
FROM mcr.microsoft.com/dotnet/runtime:6.0-alpine3.16 AS base
WORKDIR /app

# add "fontconfig" package if using "SkiaSharp.NativeAssets.Linux" in your project
# Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apk update && apk add fontconfig 

# Copy fonts from local to docker
# For example, put a "fonts" folder in your project folder, and put the font files in it,
# then, use the following line:
COPY fonts/ /usr/share/fonts

FROM mcr.microsoft.com/dotnet/sdk:6.0-alpine3.16 AS build
WORKDIR /src
COPY ["Alpine_Docker.csproj", "."]RUN dotnet restore "./Alpine_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Alpine_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Alpine_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Alpine_Docker.dll"]{{< /highlight >}}

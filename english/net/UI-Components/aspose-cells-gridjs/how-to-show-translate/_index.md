---
title: Show Translate Button and Translate Worksheet in GridJs
type: docs
weight: 260
url: /net/aspose-cells-gridjs/how-to-translate-worksheet/
description: This article explains how to enable the translate button in the GridJs toolbar and implement server‑side translation for the active worksheet.
keywords:
  - GridJs
  - translate
  - translation button
  - worksheet translation
  - AI translator
  - show translate button
aliases:
  - /net/aspose-cells-gridjs/show-translate-button/
  - /net/aspose-cells-gridjs/translate-worksheet/
  - /net/aspose-cells-gridjs/how-to-show-translate-button/
  - /net/aspose-cells-gridjs/worksheet-translation/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Introduction
The **Translate** feature adds a button to the GridJs toolbar that, when clicked, translates every string value in the active worksheet to a target locale. This guide shows how to:

1. Enable the translate button on the client side.
2. Configure the translation endpoint URL.
3. Implement a server‑side translator that complies with `Aspose.Cells.GridJs.ITextTranslator`.
4. Expose a controller action that GridJs calls to perform the translation.

> {{% alert color="primary" %}}
> The code snippets below are ready‑to‑run after you add the required NuGet packages (`Aspose.Cells.GridJs`) and register `GridJsService` in the ASP.NET Core DI container.
> {{% /alert %}}

---

## 1. Enable the Translate button on the client side  

When initializing the spreadsheet component, set **showTranslateButton** to `true` in the load options.

```javascript
// ./wwwroot/js/gridjs-init.js
const option = {
    // other options you may already use
    updateMode: 'server',
    updateUrl: '/GridJs2/UpdateCell',
    mode: 'edit',
    locale: 'en',                 // default UI language
    showTranslateButton: true     // <<< enables the translate button
};

let xs = x_spreadsheet('#gridjs-demo-uid', option);
```

### 1.1 Configure the translation endpoint  

After the spreadsheet instance is created, tell GridJs where to send the translation request.

```javascript
// Set the POST URL that will handle the translation request.
// Replace the value with the actual route you implement on the server.
xs.setTranslateUrl('/GridJs2/Translate');
```

When the user clicks the **Translate** button, GridJs will POST the required data to the URL defined above.

> {{% alert color="primary" %}}
> Ensure the endpoint URL matches the route defined in your ASP.NET Core controller.
> {{% /alert %}}

---

## 2. Server‑side implementation  

### 2.1 Create a translator that implements `ITextTranslator`

The `ITextTranslator` interface requires a single asynchronous method:

```csharp
// ./Services/MyAITranslator.cs
using System.Collections.Generic;
using System.Threading.Tasks;
using Aspose.Cells.GridJs;

namespace YourNamespace.Services
{
    /// <summary>
    /// Mock implementation of a text translator.
    /// Replace the body of <c>TranslateAsync</c> with real AI or third‑party translation logic.
    /// </summary>
    public class MyAITranslator : ITextTranslator
    {
        /// <summary>
        /// Translates a list of source texts to the target language.
        /// </summary>
        /// <param name="texts">The source strings to translate.</param>
        /// <param name="targetLanguage">ISO‑639‑1 language code (e.g., "fr", "de").</param>
        /// <returns>A list containing the translated strings in the same order.</returns>
        public async Task<List<string>> TranslateAsync(List<string> texts, string targetLanguage)
        {
            // ----- MOCK LOGIC -----
            // For demonstration we simply prepend the target language code.
            // Replace this with a call to an AI service, Google Translate, Azure Translator, etc.
            var result = new List<string>();
            foreach (var text in texts)
            {
                result.Add($"[{targetLanguage}] {text}");
            }

            // Simulate asynchronous work.
            await Task.CompletedTask;
            return result;
        }
    }
}
```

### 2.2 Expose the translation action in a controller  

```csharp
// ./Controllers/GridJsTranslateController.cs
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Aspose.Cells.GridJs;
using Microsoft.AspNetCore.Mvc;
using YourNamespace.Services;

namespace YourNamespace.Controllers
{
    [ApiController]
    [Route("GridJs2")]
    public class GridJsTranslateController : ControllerBase
    {
        // GridJsService is registered in DI (see Startup/Program).
        private readonly IGridJsService _gridJsService;

        public GridJsTranslateController(IGridJsService gridJsService)
        {
            _gridJsService = gridJsService;
        }

        /// <summary>
        /// Handles translation requests from the GridJs client.
        /// </summary>
        /// <returns>Plain‑text response containing the translated worksheet content.</returns>
        [HttpPost("Translate")]
        public async Task<IActionResult> TranslateAsync()
        {
            // 1️⃣ Read required parameters from the posted form.
            string sheet = HttpContext.Request.Form["sheet"];
            string uid   = HttpContext.Request.Form["uid"];
            string locale = HttpContext.Request.Form["locale"]; // target language code

            if (string.IsNullOrWhiteSpace(sheet) ||
                string.IsNullOrWhiteSpace(uid) ||
                string.IsNullOrWhiteSpace(locale))
            {
                return BadRequest("Missing required parameters: sheet, uid, or locale.");
            }

            // 2️⃣ Instantiate the concrete translator.
            ITextTranslator translator = new MyAITranslator();

            // 3️⃣ Invoke GridJsService to translate the entire worksheet.
            //    TranslateSheetAsync returns the translated worksheet as a string.
            string ret = await ((GridJsService)_gridJsService)
                .TranslateSheetAsync(uid, sheet, translator, locale);

            // 4️⃣ Return the result as plain text with UTF‑8 encoding.
            return Content(ret, "text/plain", Encoding.UTF8);
        }
    }
}
```

> {{% alert color="primary" %}}
> The controller expects three form fields:
> * **sheet** – the name of the worksheet to translate.
> * **uid** – the unique identifier of the workbook instance.
> * **locale** – the target language code (e.g., `fr`, `es`).
> 
> Make sure the client sends these fields exactly as shown.
> {{% /alert %}}

### 2.3 Register `GridJsService` in the DI container  

Add the service registration to `Program.cs` (or `Startup.cs` for older projects):

```csharp
// ./Program.cs
using Aspose.Cells.GridJs;

var builder = WebApplication.CreateBuilder(args);

// Register GridJs service (required for TranslateSheetAsync)
builder.Services.AddSingleton<IGridJsService, GridJsService>();

// Other service registrations …
var app = builder.Build();

// …
app.MapControllers();
app.Run();
```

---

## 3. End‑to‑end flow  

1. **Client** loads the spreadsheet with `showTranslateButton: true`.  
2. The toolbar now contains a **Translate** button.  
3. When clicked, GridJs collects all visible string values in the active worksheet and sends a POST request to `/GridJs2/Translate` (the URL set via `xs.setTranslateUrl`).  
4. **Server** receives `sheet`, `uid`, and `locale`, creates `MyAITranslator`, and calls `TranslateSheetAsync`.  
5. The translated content is returned as plain text.  
6. GridJs updates the worksheet with the translated strings automatically.

> {{% alert color="primary" %}}
> The mock translator provided here is only for demonstration. Replace its implementation with a real translation engine (e.g., Azure Cognitive Services Translator, Google Cloud Translation, or a custom AI model) to achieve production‑grade results.
> {{% /alert %}}

---

## 4. Additional notes  

* **Performance** – Translating large worksheets can be time‑consuming. Consider batching or asynchronous UI feedback (e.g., a loading spinner) on the client side.  


With these steps, you can seamlessly add multilingual support to your GridJs spreadsheets.  

---
![todo: the screen of show translate button](translate.png)
package com.legalai.controller;

import com.legalai.service.LegalService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
@RequestMapping("/api/legal")
@CrossOrigin
public class LegalController {

    @Autowired
    private LegalService service;

    @PostMapping("/analyze")
    public String analyze(@RequestParam("file") MultipartFile file) {

        return service.analyzeDocument(file);

    }

}

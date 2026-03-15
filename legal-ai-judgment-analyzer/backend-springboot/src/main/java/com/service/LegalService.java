package com.legalai.service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.http.*;

@Service
public class LegalService {

    public String analyzeDocument(MultipartFile file) {

        RestTemplate restTemplate = new RestTemplate();

        String url = "http://localhost:5001/analyze";

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.MULTIPART_FORM_DATA);

        HttpEntity<MultipartFile> request = new HttpEntity<>(file, headers);

        return restTemplate.postForObject(url, request, String.class);

    }

}

import requests
bearer_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhNcHdjdFl4YWlRdWg4Y0M0ejN0UCJ9.eyJpc3MiOiJodHRwczovL2F1dGgucmVwaHJhc2UuYWkvIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDg4ODg0ODczODk1Mjc3NTA0NjAiLCJhdWQiOlsiaHR0cHM6Ly9kaXkucmVwaHJhc2UuYWkvYXV0aDAiLCJodHRwczovL3JlcGhyYXNlYWktcHJvZC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjc5NzUwMDk2LCJleHAiOjE2Nzk4MzY0OTYsImF6cCI6IjNLVTVqdkVxV0pCQ1VLblBYMjZvbmFTUHkzakozMEo0Iiwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSByZWFkOnJlcGhyYXNlLmFpIGFsbDpkaXkgcmVhZDpyZXBocmFzZS5haSJ9.lbZjn-8CPZy-TEcByvOXyOO-tiZWaAaVjuG-GmQWGykXWnRXDEtQyyhi7qfYVvRRHJzmweMgRZVsYUHannzPV85-lGgmpIB1IzkBeRO_zz4xtviISB1ndu_wrR12mixKbKqpoDZRnld53YpUWRtT4BVW8RT1C2_Fb2f8W83FAdSLE9bGcwaYx47a8FkAE43KL1dKxvuF6K65UEwdTP0GVkixoGtkyVON2XbrLVof0gnYeo86DwaWXu4-1sXTyAo7kCNwJhg809C-vOLp1UKG3UTIoT9sPTRdhYDKS6oBzL6JUBT2thEaUK39TvI_UncC1NCejOUlpeSCexpWT0nOaw"
url = "https://personalized-brand.api.rephrase.ai/v2/campaign/create"

payload = {
    "videoDimension": {
        "height": 1080,
        "width": 1920
    },
    "scenes":
    [
        {
            "elements":
            [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://rephrase-assets.s3.ap-south-1.amazonaws.com/media/panel_defaults/background/image/blue_1.webp"
                    }
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em"
                    },
                    "asset": {
                        "kind": "Spokesperson",
                        "spokespersonVideo": {
                            "output_params": {"video": {
                                "resolution": {
                                    "height": 720,
                                    "width": 1280
                                },
                                "background": {"alpha": 0},
                                "crop": {"preset": "MS"}
                            }},
                            "model": "george_retrain_nt",
                            "voiceId": "en-IN-Wavenet-B__007",
                            "gender": "male",
                            "transcript": "<speak>  Hi, I am Ayush Kumar and I'm thrilled to apply for the SDE Intern position at Rephrase dot ai.I'm currently pursuing my Bachelor's degree in Mining engineering  with 9.08 cpi.</speak>",
                            "transcript_type": "ssml_limited"
                        },

                    },
                },

            ]
        },
        {
            "elements":
            [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://rephrase-assets.s3.ap-south-1.amazonaws.com/media/panel_defaults/background/image/blue_1.webp"
                    }
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em"
                    },
                    "asset": {

                        "spokespersonVideo": {
                            "output_params": {"video": {
                                "resolution": {
                                    "height": 720,
                                    "width": 1280
                                },
                                "background": {"alpha": 0},
                                "crop": {"preset": "MS"}
                            }},
                            "model": "george_retrain_nt",
                            "voiceId": "en-IN-Wavenet-B__007",
                            "gender": "male",
                            "transcript": "<speak> And I've completed courses in Data Structures, Algorithms, and Object-Oriented Programming. During my studies, I've developed a strong foundation in programming languages such as C, C++, HTML, CSS, JavaScript,  also I have interest  in Competitive Programming, Web Development,  and have learned to work with various software development tools such as Git .</speak>",
                            "transcript_type": "ssml_limited"
                        },
                        "kind": "Spokesperson",
                    }
                },
                {
                    "style": {
                        "variant": "subheading",
                        "fontSize": "4.777777777777778em",
                        "fontFamily": "Roboto",
                        "color": "#FFFFFF",
                        "position": "absolute",
                        "zIndex": 15,
                        "align": "left",
                        "height": "5.912361095419285em",
                        "width": "30.170754733240013em",
                        "bottom": "33.28846002860913em",
                        "left": "12.064089036806962em",
                        "fontColor": "#631111",
                        "textDecorationColor": "#631111"
                    },
                    "asset": {
                        "textStyle": {
                            "fontColor": "#631111",
                            "fontSize": "4.777777777777778em",
                            "textDecorationColor": "#631111"
                        },
                        "kind": "Text",
                        "text": " Languages: C, C++, HTML, CSS, JavaScript "
                        "Interests: Data Structure, Algorithms, Competitive Programming, Web Development, OOPs"

                    },
                },
            ]
        },

        {
            "elements":
            [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://rephrase-assets.s3.ap-south-1.amazonaws.com/media/panel_defaults/background/image/blue_1.webp"
                    }
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em"
                    },
                    "asset":
                    {
                        "spokespersonVideo": {
                            "output_params": {"video": {
                                "resolution": {
                                    "height": 720,
                                    "width": 1280
                                },
                                "background": {"alpha": 0},
                                "crop": {"preset": "MS"}
                            }},
                            "model": "george_retrain_nt",
                            "voiceId": "en-IN-Wavenet-B__007",
                            "gender": "male",
                            "transcript": "<speak> I'm a quick learner and I'm eager to apply my knowledge to real-world projects. I've worked on various personal projects, such as Foodie ( A recipe website) which uses The Meal DB API which Incorporated features including searching for meals by name, looking up complete meal facts using an ID, and searching for a single random meal.Also I have Created user interface (UI) for a music website named Whistle ( a clone of Spotify) that that is aesthetically pleasing and offers a good experience. Used audio API of JavaScript, Incorporated features play, pause, sync with track, navigate to previous and next track. </speak>",
                            "transcript_type": "ssml_limited"
                        },
                        "kind": "Spokesperson",

                    }
                },
                {
                    "style": {
                        "variant": "subheading",
                        "fontSize": "4.777777777777778em",
                        "fontFamily": "Roboto",
                        "color": "#FFFFFF",
                        "position": "absolute",
                        "zIndex": 15,
                        "align": "left",
                        "height": "5.912361095419285em",
                        "width": "30.170754733240013em",
                        "bottom": "33.28846002860913em",
                        "left": "12.064089036806962em",
                        "fontColor": "#631111",
                        "textDecorationColor": "#631111"
                    },
                    "asset": {
                        "textStyle": {
                            "fontColor": "#631111",
                            "fontSize": "4.777777777777778em",
                            "textDecorationColor": "#631111"
                        },
                        "kind": "Text",
                        "text": " Projects: Foodie -A reciepe app) "
                                "whistle: A clone of spotify"

                    },
                },
            ]
        },
        {
            "elements":
            [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://rephrase-assets.s3.ap-south-1.amazonaws.com/media/panel_defaults/background/image/blue_1.webp"
                    }
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em"
                    },
                    "asset":
                    {
                        "spokespersonVideo": {
                            "output_params": {"video": {
                                "resolution": {
                                    "height": 720,
                                    "width": 1280
                                },
                                "background": {"alpha": 0},
                                "crop": {"preset": "MS"}
                            }},
                            "model": "george_retrain_nt",
                            "voiceId": "en-IN-Wavenet-B__007",
                            "gender": "male",
                            "transcript": "<speak> I'm a team player and I enjoy collaborating with others to solve problems. I'm currently a member of my university's coding club, where we work on programming challenges and participate in hackathons. I've also contributed to open-source projects on GitHub and Stack Overflow, where I've gained experience in working with distributed teams and version control systems.In my college I have worked with different clubs and council and also worked at the different position like I am the Joint secretary of the mining society also I am Opertional manager at kashiyatra the  annual cultural fest of IIT BHU.</speak>",
                            "transcript_type": "ssml_limited"
                        },
                        "kind": "Spokesperson",

                    }
                },
                {
                    "style": {
                        "variant": "subheading",
                        "fontSize": "4.777777777777778em",
                        "fontFamily": "Roboto",
                        "color": "#FFFFFF",
                        "position": "absolute",
                        "zIndex": 15,
                        "align": "left",
                        "height": "5.912361095419285em",
                        "width": "30.170754733240013em",
                        "bottom": "33.28846002860913em",
                        "left": "12.064089036806962em",
                        "fontColor": "#631111",
                        "textDecorationColor": "#631111"
                    },
                    "asset": {
                        "textStyle": {
                            "fontColor": "#631111",
                            "fontSize": "4.777777777777778em",
                            "textDecorationColor": "#631111"
                        },
                        "kind": "Text",
                        "text": " Position of responsibility "
                                "Joint secretary- Mining society"
                                "Operational manager- Kashiyatra"

                    },
                },
            ]
        },
         {
            "elements":
            [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://rephrase-assets.s3.ap-south-1.amazonaws.com/media/panel_defaults/background/image/blue_1.webp"
                    }
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em"
                    },
                    "asset": {
                        "kind": "Spokesperson",
                        "spokespersonVideo": {
                            "output_params": {"video": {
                                "resolution": {
                                    "height": 720,
                                    "width": 1280
                                },
                                "background": {"alpha": 0},
                                "crop": {"preset": "MS"}
                            }},
                            "model": "george_retrain_nt",
                            "voiceId": "en-IN-Wavenet-B__007",
                            "gender": "male",
                            "transcript": "<speak>  I'm excited about the opportunity to work with the experienced developers at Rephrase dot ai and gain hands-on experience in software development. Thank you for considering my application.</speak>",
                            "transcript_type": "ssml_limited"
                        },

                    },
                },

            ]
        },
        


    ],
    "title": "16:9 Widescreen",
    "thumbnailUrl": "https://rephrase-assets.s3.ap-south-1.amazonaws.com/template_thumbnails/cold_reachout_1.png"
}
headers = {
    "accept": "application/json",
    "Authorization": bearer_token,
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)

# Plagarism-Detection-Tool
PlagiarismGuard AI is a web-based plagiarism detection system designed to analyze and compare documents for content similarity. The application helps users identify potential plagiarism by processing and evaluating text from multiple file formats, including PDF, DOCX, and TXT files.

The system is built using Python and Flask on the backend, where users can securely log in, upload documents, and receive detailed similarity reports. Advanced Natural Language Processing (NLP) techniques are employed through scikit-learn’s TF-IDF Vectorizer and Cosine Similarity algorithms to calculate accurate similarity percentages between documents.

PlagiarismGuard AI extracts text from uploaded files, compares the content, and categorizes the results into risk levels such as Low, Medium, and High based on the degree of similarity detected. All analysis results and user information are securely managed using a MySQL database.

The frontend is developed using HTML, CSS, and JavaScript, providing an intuitive and user-friendly interface for document submission and result visualization. A dedicated dashboard displays historical plagiarism-check statistics and similarity distributions through interactive Chart.js visualizations. Additionally, users can export generated reports for future reference and documentation.

Overall, PlagiarismGuard AI offers an efficient, accurate, and accessible solution for plagiarism detection, making it suitable for students, educators, researchers, and organizations seeking to maintain content originality and academic integrity.


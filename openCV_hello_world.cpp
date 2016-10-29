
// Open CV Dependencies
#include <opencv2/highgui/highgui.hpp>
#ifdef OPENCV3
#include <opencv2/imgproc.hpp>
#endif
int main() {
  // 512 rows, 512 columns
  cv::Mat img(512, 512, CV_8UC3, cv::Scalar(0));
  
  cv::putText(img, 
    "Hi from Jetson and OpenCV!!",
    cv::Point(10, img.rows / 2), // top left corner for text box
    cv::FONT_HERSHEY_DUPLEX, // font
    1.0, // scaling factor
    CV_RGB(118,185,0), // color
    2); // thickness

  cv::imshow("Hi!", img); // Title and image to show
  cv::waitKey(); // wait for key before exiting

}

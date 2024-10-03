import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Review } from "../types";

interface ReviewCardProps {
  review: Review;
}

const ReviewCard: React.FC<ReviewCardProps> = ({ review }) => {
  return (
    <Card>
      <CardContent className="p-4">
        <p className="font-semibold">{review.user.username}</p>
        <p>Rendering: {review.rendering_rating}/5</p>
        <p>Anatomy: {review.anatomy_rating}/5</p>
        <p>Composition: {review.composition_rating}/5</p>
        <p>Overall: {review.global_rating.toFixed(1)}/5</p>
        {review.rendering_comment && (
          <p>Rendering: {review.rendering_comment}</p>
        )}
        {review.anatomy_comment && <p>Anatomy: {review.anatomy_comment}</p>}
        {review.composition_comment && (
          <p>Composition: {review.composition_comment}</p>
        )}
      </CardContent>
    </Card>
  );
};

export default ReviewCard;
